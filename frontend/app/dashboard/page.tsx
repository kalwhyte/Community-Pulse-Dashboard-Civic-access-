'use client'

import { useEffect, useState } from 'react'
import SummaryCards from '../../components/SummaryCards'
import MismatchChart from '../../components/MismatchChart'
import InsightPanel from '../../components/InsightPanel'
import CrawlRunner from '../../components/CrawlRunner'

export default function Dashboard() {
  const [data, setData] = useState(null)

  useEffect(() => {
    // Fetch data from backend
    fetch('/api/dashboard/summary')
      .then(res => res.json())
      .then(setData)
  }, [])

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-8">Dashboard</h1>
      <SummaryCards data={data} />
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <MismatchChart />
        <InsightPanel />
      </div>
      <CrawlRunner />
    </div>
  )
}
