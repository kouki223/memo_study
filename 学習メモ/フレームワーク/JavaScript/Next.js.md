# Next.js

## ディレクトリに応じてルーティングされる

## APIの表現方法
Next.js Route Handlersという機能を使う方法
app/apiディレクトリにファイルを配置する事でAPIエンドポイントを表現する事が出来る

[エンドポイント]
GET /api/users
POST /api/users
GET /api/users/[id]
PUT /api/users/[id]
DELETE /api/users/[id]

project-root/
├── app/
│   ├── api/
│   │   ├── users/
│   │   │   ├── [id]/
│   │   │   │   └── route.ts
│   │   │   └── route.ts

```javascript
import { NextRequest, NextResponse } from "next/server";

// app/api/book/route.js
export async function GET() {
  return Response.json([{ id: 1, title: "よくわかるNext.js" }]);
}

export async function POST(req) {
  const { title } = await req.json();
  return Response.json({ id: 2, title }, { status: 201 });
}
```
上記のようにbookAPIに対してGETとPOSTの時の挙動を定義する

app/api/book/[id]/route.js
```javascript
import { NextRequest, NextResponse } from "next/server";

// app/api/book/[id]/route.js
export async function GET(req, { params }) {
  const { id } = params;
  return Response.json({ id, title: `Book ${id}` });
}
```

クエリパラメーターを含むリクエスト
```javascript
// ...
// 例）GET /api/users?query=hoge のようなリクエストの場合
export function GET(request: NextRequest): NextResponse {
  const params = request.nextUrl.searchParams;
  const query = params.get("query");
  // query = "hoge"
// ...
```

リクエストボディの処理
```javascript
// ...
// 例）POST /api/users (request body: {"key": "hoge"}) のようなリクエストの場合
export async function POST(request: NextRequest): Promise<NextResponse> {
  const params = await request.json();
  // params = {key: "hoge"}
// ...
```

CORSの設定

```javascript
export function GET(request: NextRequest): NextResponse {
    return NextResponse.json(
        { response: "Test response." },
        {
          status: 200,  // ステータスコード
          headers: {    // レスポンスヘッダー
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, Authorization",
          },
        },
  );
}
```

開発サーバーを立てる
↑
何かの環境へデプロイする
↑
コンテナ化しておく事で良い影響が多くある

```Dockerfile
FROM node:20-alpine AS base

# Install dependencies only when needed
FROM base AS deps
# Check https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine to understand why libc6-compat might be needed.
RUN apk add --no-cache libc6-compat
WORKDIR /app

# Install dependencies based on the preferred package manager
COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* ./
RUN \
  if [ -f yarn.lock ]; then yarn --frozen-lockfile; \
  elif [ -f package-lock.json ]; then npm ci; \
  elif [ -f pnpm-lock.yaml ]; then yarn global add pnpm && pnpm i --frozen-lockfile; \
  else echo "Lockfile not found." && exit 1; \
  fi

# Rebuild the source code only when needed
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .

RUN npm run build

# Production image, copy all the files and run next
FROM base AS runner
WORKDIR /app

ENV NODE_ENV production

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public

# Set the correct permission for prerender cache
RUN mkdir .next
RUN chown nextjs:nodejs .next

# Automatically leverage output traces to reduce image size
# https://nextjs.org/docs/advanced-features/output-file-tracing
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000

ENV PORT 3000
ENV HOSTNAME "0.0.0.0"

# server.js is created by next build from the standalone output
# https://nextjs.org/docs/pages/api-reference/next-config-js/output
CMD ["node", "server.js"]
```

コンテナビルド => docker run -p 3000:3000 next-rest-api-sample

Nexxt.js で REST APIが実装出来るという事

# Server Actions
APIルート（Route Handlers）を作成せずに、サーバー側の処理を直接呼び出せる仕組み
- 使い分け

fetchを使ったREST APIは型の管理やエンドポイントの実装が必要。
Server ActionsはJSの関数のように呼び出せ、主にデータ更新に特化している。

- 裏側の仕組み

ビルド時にユニークなアクションIDが割り振られる。
クライアント実行時には <input type="hidden"> などで自動生成され、Next-Actionヘッダーを付与したPOSTリクエストが自動で送信される。

