const updateLogs = (e) => {
    const selected_car = document.getElementById('carDropdown').value
    filterTable(selected_car)
}

const filterTable = (selected_car) => {
    const rows = document.querySelectorAll("#vehicleTable tbody tr")
    rows.forEach(row => {
        const vehicleType = row.getAttribute('data-vehicle')
        if (selected_car === 'all' || selected_car === vehicleType) {
            row.style.display = '';
        } else {
            row.style.display = 'none'
        }
    })
}