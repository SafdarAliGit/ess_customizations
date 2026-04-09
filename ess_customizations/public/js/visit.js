frappe.ui.form.on('Visit', {

    refresh(frm) {
        setTimeout(() => {
            frm.trigger('sync_location_to_map');
        }, 800);
    },

    location(frm) {
        setTimeout(() => {
            frm.trigger('sync_location_to_map');
        }, 300);
    },

    custom_log_location(frm) {
        frm.trigger('sync_location_to_map');
    },

    sync_location_to_map(frm) {
        const loc = frm.doc.location;
        if (!loc || !loc.includes(',')) return;

        const [lat, lng] = loc.split(',').map(parseFloat);
        if (isNaN(lat) || isNaN(lng)) return;

        const geoValue = JSON.stringify({
            type: "FeatureCollection",
            features: [{
                type: "Feature",
                properties: {},
                geometry: {
                    type: "Point",
                    coordinates: [lng, lat]   // GeoJSON = [lng, lat]
                }
            }]
        });

        // Set value on the doc directly and refresh the field
        frm.doc.custom_map = geoValue;
        frm.get_field('custom_map').set_value(geoValue);
        frm.refresh_field('custom_map');

        // After field re-renders, zoom into the point and show description
        setTimeout(() => {
            const field = frm.get_field('custom_map');
            if (!field || !field.map) return;

            field.map.setView([lat, lng], 15);

            // Show description overlay on map corner
            const mapContainer = field.map.getContainer();

            // Remove existing overlay if any
            const existing = mapContainer.querySelector('.visit-map-description');
            if (existing) existing.remove();

            const log_location = frm.doc.custom_log_location;
            if (log_location && log_location.trim()) {
                const overlay = document.createElement('div');
                overlay.className = 'visit-map-description';
                overlay.style.cssText = `
                    position: absolute;
                    bottom: 0;
                    right: 0;
                    z-index: 1000;
                    max-width: 280px;
                    background: rgba(255, 255, 255, 0.96);
                    backdrop-filter: blur(8px);
                    -webkit-backdrop-filter: blur(8px);
                    border-radius: 10px 0 0 0;
                    box-shadow: -3px -3px 18px rgba(94,100,255,0.10);
                    padding: 12px 16px;
                    font-size: 13px;
                    color: #2d2d2d;
                    line-height: 1.6;
                    pointer-events: none;
                    border-top: 3px solid var(--primary, #5e64ff);
                    border-left: 3px solid var(--primary, #5e64ff);
                    letter-spacing: 0.2px;
                `;
                overlay.innerHTML = `
                    <div style="display:flex;align-items:flex-start;gap:8px;">
                        <span style="margin-top:5px;flex-shrink:0;width:7px;height:7px;border-radius:50%;background:var(--primary,#5e64ff);box-shadow:0 0 8px rgba(94,100,255,0.5);display:inline-block;"></span>
                        <span style="word-break:break-word;">${frappe.utils.escape_html(log_location.trim())}</span>
                    </div>
                `;
                mapContainer.style.position = 'relative';
                mapContainer.appendChild(overlay);
            }

        }, 600);
    }

});