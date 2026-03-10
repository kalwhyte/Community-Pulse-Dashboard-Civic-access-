'use client'

import { useState } from 'react'

export default function CrawlRunner() {
  const [url, setUrl] = useState('')

  const handleCrawl = () => {
    // Placeholder for calling backend
    alert(`Crawling ${url}`)
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
