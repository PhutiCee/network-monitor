import { useEffect, useState } from "react";
import { connectWebSocket } from "./services/api";

import BandwidthChart from "./components/BandwidthChart";
import ProtocolPie from "./components/ProtocolPie";
import TopTalkers from "./components/TopTalkers";
import Connections from "./components/Connections";

function App() {
  const [data, setData] = useState({
    bandwidth: [],
    protocols: {},
    top_talkers: {},
    connections: 0,
  });

  useEffect(() => {
    connectWebSocket((incomingData) => {
      setData(incomingData);
    });
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Network Monitoring Dashboard</h1>

      <Connections count={data.connections} />

      <BandwidthChart data={data.bandwidth} />

      <ProtocolPie data={data.protocols} />

      <TopTalkers data={data.top_talkers} />
    </div>
  );
}

export default App;
