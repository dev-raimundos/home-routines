# Guia de Setup e Execução

## 2. Construir o Worker

Para montar a imagem que contém os drivers do Oracle e o Playwright:

```bash
task build-worker
```

---

## 3. Subir a Infraestrutura

```bash
task up
```

* Airflow disponível em: [http://localhost:8080](http://localhost:8080)
  **User:** admin
  **Password:** admin

* Dozzle (logs em tempo real): [http://localhost:8888](http://localhost:8888)

---

## Estrutura de Pastas

```plaintext
.
├── airflow/            # Configurações, DAGs e logs do Airflow
│   ├── dags/           # Ficheiros de agendamento
│   └── logs/           # (Ignorado no Git) Logs das tasks
├── scripts/            # Scripts de automação (core do RPA)
│   ├── common/         # Classes base e utilitários
│   └── rpa_web/        # Scripts específicos (Playwright)
├── workers/            # Dockerfile e drivers do worker especializado
│   └── drivers/        # Oracle Instant Client (.zip)
├── Taskfile.yml        # Automação de comandos (tipo Makefile)
└── docker-compose.yml  # Definição dos serviços
```

---

## Testar Conexão Oracle

Para validar o funcionamento do Instant Client dentro do container:

```bash
docker run --rm -it \
  --network airflow_automation-net \
  -v $(pwd)/scripts:/app/scripts \
  -e DB_USER=teu_user \
  -e DB_PASS=tua_senha \
  rpa-worker:latest python scripts/test_oracle.py
```

---

## Boas Práticas (Guia do Mentor)

### Segurança

Nunca coloques credenciais no código.
Utiliza `.env` ou **Airflow Connections**.

### Idempotência

Os scripts devem poder falhar e reiniciar sem duplicar dados no Oracle.

### Logs

Utiliza o Dozzle para monitorizar execuções em tempo real durante o desenvolvimento.

### Permissões

Se houver problemas de escrita:

```bash
task setup
```

Isso reseta os proprietários das pastas (UID 50000).

---

## Manutenção

**Mantido por:**
Raimundos Marques da Silva Neto
*Lead Software Engineer / Architect*

---

## Próximos Passos

* Criar uma **BaseAutomation (classe base)** para padronizar:

  * Conexão Oracle (modo Thick)
  * Setup do Playwright
  * Tratamento de erros (screenshots automáticos)
  * Logging integrado com Airflow

---
