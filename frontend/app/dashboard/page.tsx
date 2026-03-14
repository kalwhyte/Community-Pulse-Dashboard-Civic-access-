"use client";

import { useEffect, useMemo, useState } from "react";
import SummaryCards from "../../components/SummaryCards";
import MismatchChart from "../../components/MismatchChart";
import InsightPanel from "../../components/InsightPanel";
import CrawlRunner from "../../components/CrawlRunner";

type SummaryResponse = {
  city: string;
  top_issue: string;
  average_sentiment: number;
  mismatch_hotspots: number;
};

type Insight = {
  location: string;
  category: string;
  social_score: number;
  official_score: number;
  mismatch_score: number;
  explanation: string;
};

export default function Dashboard() {
  const apiBase = useMemo(
    () =>
      process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000/api/v1",
    [],
  );
  const [summary, setSummary] = useState<SummaryResponse | null>(null);
  const [insights, setInsights] = useState<Insight[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const controller = new AbortController();

    Promise.all([
      fetch(`${apiBase}/dashboard/summary`, { signal: controller.signal }).then(
        (res) =>
          res.ok
            ? res.json()
            : Promise.reject(new Error("Failed to load summary")),
      ),
      fetch(`${apiBase}/dashboard/insights`, {
        signal: controller.signal,
      }).then((res) =>
        res.ok
          ? res.json()
          : Promise.reject(new Error("Failed to load insights")),
      ),
    ])
      .then(([summaryData, insightsData]) => {
        setSummary(summaryData);
        setInsights(insightsData);
      })
      .catch((err: Error) => {
        if (err.name !== "AbortError") {
          setError(err.message);
        }
      });

    return () => controller.abort();
  }, [apiBase]);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-8">Dashboard</h1>
      {error && (
        <div className="mb-6 rounded border border-red-200 bg-red-50 p-3 text-sm text-red-700">
          {error}
        </div>
      )}
      <SummaryCards data={summary} />
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <MismatchChart insights={insights} />
        <InsightPanel insights={insights} />
      </div>
      <CrawlRunner apiBase={apiBase} />
    </div>
  );
}
