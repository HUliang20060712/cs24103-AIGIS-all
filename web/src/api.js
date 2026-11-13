// 统一经网关访问：dev 8081 / test 8082 / prod 80
const BASE = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:8081';

export function streamChat(payload, onChunk, onDone) {
  const ctrl = new AbortController();
  fetch(`${BASE}/api/chat/stream`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
    signal: ctrl.signal,
  }).then(async (resp) => {
    const reader = resp.body.getReader();
    const decoder = new TextDecoder();
    let buf = '';
    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      buf += decoder.decode(value, { stream: true });
      const lines = buf.split('\n\n');
      buf = lines.pop() || '';
      for (const line of lines) {
        if (line.startsWith('data:')) onChunk(line.slice(5).trim());
      }
    }
    onDone();
  }).catch((e) => {
    if (e.name !== 'AbortError') onChunk(`[连接中断] ${e.message}`);
    onDone();
  });
  return () => ctrl.abort();
}

export async function fetchFeed(userId, page = 1, size = 10) {
  const r = await fetch(`${BASE}/api/reco/feed?userId=${userId}&page=${page}&size=${size}`);
  if (!r.ok) throw new Error(`feed ${r.status}`);
  return r.json();
}
