export const GET = () => {
	const encoder = new TextEncoder();
	let closed = false;

	const stream = new ReadableStream({
		start(controller) {
			const interval = setInterval(() => {
				if (closed) return;

				const now = new Date().toISOString();
				const temperature = (Math.random() * (330 - 270) + 270).toFixed(2);
				const boron = (Math.random() * 2500).toFixed(1);
				const neutronFlux = (Math.random() * (1e14 - 1e12) + 1e12).toExponential(2);
				const line = `${now},${temperature},${boron},${neutronFlux}`;

				try {
					controller.enqueue(encoder.encode(`data: ${line}\n\n`));
				} catch {
					console.error('Stream already closed');
					clearInterval(interval);
				}
			}, 1000);  // her saniyede bir veri gönder

			// Akış istemci tarafından iptal edilince çağrılır
			this.cancel = () => {
				closed = true;
				clearInterval(interval);
				controller.close();
			};
		}
	});

	return new Response(stream, {
		headers: {
			'Content-Type': 'text/event-stream',
			'Cache-Control': 'no-cache',
			Connection: 'keep-alive'
		}
	});
};
