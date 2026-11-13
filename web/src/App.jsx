import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import { streamChat } from './api.js';

export default function App() {
  const [q, setQ] = useState('');
  const [msgs, setMsgs] = useState([]);
  const [busy, setBusy] = useState(false);

  function send() {
    if (!q.trim() || busy) return;
    const question = q.trim();
    setMsgs((m) => [...m, { role: 'user', text: question }, { role: 'ai', text: '' }]);
    setQ('');
    setBusy(true);
    streamChat({ question, history: msgs.slice(-6) }, (chunk) => {
      setMsgs((m) => {
        const copy = [...m];
        copy[copy.length - 1] = { role: 'ai', text: copy[copy.length - 1].text + chunk };
        return copy;
      });
    }, () => setBusy(false));
  }

  return (
    <div style={{ maxWidth: 860, margin: '40px auto', fontFamily: 'sans-serif' }}>
      <h2>AIGIS 智能地理信息问答</h2>
      {msgs.map((m, i) => (
        <div key={i} style={{ margin: '12px 0', textAlign: m.role === 'user' ? 'right' : 'left' }}>
          <div style={{ display: 'inline-block', padding: '10px 14px', borderRadius: 8,
                        background: m.role === 'user' ? '#e8f1ff' : '#f4f4f4', textAlign: 'left' }}>
            {m.role === 'ai' ? <ReactMarkdown>{m.text || '…'}</ReactMarkdown> : m.text}
          </div>
        </div>
      ))}
      <div style={{ display: 'flex', gap: 8, marginTop: 20 }}>
        <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="问问这块地的地物类型"
               style={{ flex: 1, padding: 10 }} onKeyDown={(e) => e.key === 'Enter' && send()} />
        <button onClick={send} disabled={busy}>{busy ? '生成中' : '发送'}</button>
      </div>
    </div>
  );
}
