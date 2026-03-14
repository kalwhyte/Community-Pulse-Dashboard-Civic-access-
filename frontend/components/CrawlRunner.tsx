'use client'

import { useState } from 'react'

<<<<<<< HEAD
<<<<<<< HEAD
type CrawlRunnerProps = {
  apiBase: string
}

export default function CrawlRunner({ apiBase }: CrawlRunnerProps) {
  const [url, setUrl] = useState('')
  const [status, setStatus] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [isLoading, setIsLoading] = useState(false)

  const handleCrawl = async () => {
    if (!url.trim()) {
      setError('Please enter a URL to crawl.')
      return
    }

    setIsLoading(true)
    setStatus(null)
    setError(null)

    try {
      const response = await fetch(`${apiBase}/ingest/social`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ urls: [url.trim()] }),
      })

      if (!response.ok) {
        throw new Error('Crawl request failed')
      }

      const result = await response.json()
      setStatus(`Snapshot ID: ${result.snapshot_id ?? 'unknown'}`)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Crawl failed')
    } finally {
      setIsLoading(false)
    }
=======
=======
>>>>>>> ed222926a3315889b3f9d74acf5ffc2f73767928
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
<<<<<<< HEAD
>>>>>>> a7dd7179371cf60abafa5351a198e4f19a3b22ff
=======
>>>>>>> ed222926a3315889b3f9d74acf5ffc2f73767928
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
      <button
        onClick={handleCrawl}
        disabled={isLoading}
        className="bg-blue-500 text-white px-4 py-2 rounded disabled:opacity-50"
      >
        {isLoading ? 'Crawling...' : 'Crawl'}
      </button>
      {status && <p className="mt-3 text-sm text-green-700">{status}</p>}
      {error && <p className="mt-3 text-sm text-red-600">{error}</p>}
    </div>
  )
}
