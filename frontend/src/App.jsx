import { useEffect, useState } from "react";
import { connectWebSocket } from "./services/api";

import DashboardLayout from "./components/DashboardLayout";
import AlertBanner from "./components/AlertBanner";
import Card from "./components/Card";

import BandwidthChart from "./components/BandwidthChart";
import ProtocolPie from "./components/ProtocolPie";
import TopTalkers from "./components/TopTalkers";
import SystemHealth from "./components/SystemHealth";
import Connections from "./components/Connections";
import BandwidthRate from "./components/BandwidthRate";
import PPS from "./components/PPS";

function App() {
  const [data, setData] = useState({
    bandwidth: [],
    protocols: {},
    top_talkers: {},
    connections: 0,
    alerts: [],
    bandwidth_rate: 0,
    pps: 0,
  });

  useEffect(() => {
    connectWebSocket((incomingData) => {
      setData((prev) => ({ ...prev, ...incomingData }));
    });
  }, []);

  return (
    <DashboardLayout>
      {/* 🚨 ALERTS */}
      <AlertBanner alerts={data.alerts} />

      <SystemHealth data={data} />
      <Connections count={data.connections} />
      {/* KPI ROW */}
      <Card
        title="Bandwidth Rate"
        value={data.bandwidth_rate?.toFixed(2)}
        unit="B/s"
      />
      <Card title="Packets/sec" value={data.pps?.toFixed(2)} unit="pps" />

      {/* CHARTS */}
      <BandwidthChart data={data.bandwidth} />
      <ProtocolPie data={data.protocols} />

      {/* DETAILS */}
      <TopTalkers data={data.top_talkers} />
    </DashboardLayout>
  );
}

export default App;
