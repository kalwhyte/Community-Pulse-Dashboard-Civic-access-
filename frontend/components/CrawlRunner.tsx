'use client'

import { useState } from 'react'

type Props = {
  apiBase: string
}

export default function CrawlRunner({ apiBase }: Props) {
  const [url, setUrl] = useState('')

  const handleCrawl = async () => {
  if (!url) return

  try {
    const res = await fetch(`${apiBase}/ingest/social`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        urls: [url]
      })
    })

    if (!res.ok) throw new Error("Crawl failed")

    const data = await res.json()

    alert(`Snapshot started: ${data.snapshot_id}`)
  } catch (err) {
    alert("Failed to start crawl")
  }
}

  return (
    <div className="bg-white p-4 rounded shadow mt-8">
      <h3 className="text-lg font-semibold mb-4">Run Crawl</h3>
      <input
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter URL to crawl"
        className="border p-2 w-full mb-4"
      />
      <button onClick={handleCrawl} className="bg-blue-500 text-white px-4 py-2 rounded">
        Crawl
      </button>
    </div>
  )
}
