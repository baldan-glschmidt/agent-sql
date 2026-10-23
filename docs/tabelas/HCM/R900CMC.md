# R900CMC

## Descrição

Registro de comandos SQL em ambientes Cloud

---

## Resumo

- Campos: 5
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| USRNAM | String(255) | Sim | Usuário Executor do comando SQL em ambiente CLOUD |
| CMDEXE | String(9999) | Sim | Comando SQL que foi executado em ambiente CLOUD |
| OPECMD | String(255) | Sim | Descrição comando SQL que foi executado em ambiente CLOUD |
| EXEDAT | Date | Sim | Data de execução do comando SQL que foi executado em ambiente CLOUD |
| QTDAFE | Number(009,0) | Sim | QTD Registros afetados pelo comando SQL no ambiente CLOUD |

---

## Chave Primária

Não possui.

---

## Índices

### R900CMCUSRNAMEXEDAT

**Tipo:** Não unico

Campos:
- USRNAM
- EXEDAT

---

## Relacionamentos

Nenhum relacionamento cadastrado.
