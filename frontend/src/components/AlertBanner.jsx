function AlertBanner({ alerts }) {
  if (!alerts || alerts.length === 0) return null;

  return (
    <div style={styles.banner}>
      <h3>🚨 Active Network Alerts</h3>

      {alerts.slice(-3).map((a, i) => (
        <div key={i} style={styles.alert}>
          {a.message}
        </div>
      ))}
    </div>
  );
}

const styles = {
  banner: {
    gridColumn: "1 / -1",
    backgroundColor: "#7f1d1d",
    padding: "15px",
    borderRadius: "10px",
    marginBottom: "10px",
    border: "1px solid #ef4444",
  },

  alert: {
    marginTop: "5px",
    fontSize: "14px",
    color: "#fecaca",
  },
};

export default AlertBanner;
