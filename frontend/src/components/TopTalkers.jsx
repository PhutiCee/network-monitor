function TopTalkers({ data }) {
  const entries = Object.entries(data)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5);

  return (
    <div>
      <h2>Top Talkers</h2>
      <ul>
        {entries.map(([ip, bytes]) => (
          <li key={ip}>
            {ip} — {bytes} bytes
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TopTalkers;
