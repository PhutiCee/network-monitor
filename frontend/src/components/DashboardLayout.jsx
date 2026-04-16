function DashboardLayout({ children }) {
  return (
    <div style={styles.container}>
      {/* HEADER */}
      <div style={styles.header}>
        <h1>Network Monitoring System</h1>
        <div style={styles.live}>🟢 LIVE</div>
      </div>

      {/* GRID */}
      <div style={styles.grid}>{children}</div>
    </div>
  );
}

const styles = {
  container: {
    backgroundColor: "#0b1220",
    minHeight: "100vh",
    color: "white",
    fontFamily: "Arial",
    padding: "20px",
  },

  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: "20px",
    padding: "10px 0",
    borderBottom: "1px solid #1f2937",
  },

  live: {
    backgroundColor: "#16a34a",
    padding: "6px 12px",
    borderRadius: "20px",
    fontSize: "12px",
    fontWeight: "bold",
  },

  grid: {
    display: "grid",
    gridTemplateColumns: "1fr 1fr",
    gap: "20px",
  },
};

export default DashboardLayout;
