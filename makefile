format:
	isort .
	ruff format

serve:
	vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-7B \
		--served-model-name deepseek-r1 \
		--dtype half \
		--max-model-len 65536 \
		--max-num-seqs 1 \
		--enable-auto-tool-choice \
		--tool-call-parser hermes \
		--guided-decoding-backend=lm-format-enforcer

serve_qwen:
	vllm serve Qwen/Qwen2.5-7B-Instruct \
		--served-model-name qwen \
		--dtype half \
		--max-num-seqs 1 \
		--enable-auto-tool-choice \
		--tool-call-parser hermes \
		--guided-decoding-backend=lm-format-enforcer
