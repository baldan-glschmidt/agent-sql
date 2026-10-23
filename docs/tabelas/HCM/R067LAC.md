# R067LAC

## Descrição

Log Acertos Apuração

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DtHLog | Number(014,6) | Não | Data/Hora do Log de Acertos |
| CnxUsu | Number(005,0) | Não | Número da Conexão do Usuário |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| DatApu | Date | Sim | Data da Apuração |
| MsgLog | String(300) | Sim | Mensagem do Log de Acertos |
| AceRto | String(001) | Sim | Realizado Acerto Retroativo |
| AceRep | String(001) | Sim | Acerto Retroativo com Integração Reprocessada |

---

## Chave Primária

- DtHLog
- CnxUsu

---

## Índices

### R067LACInidice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- DatApu

---

## Relacionamentos

Nenhum relacionamento cadastrado.
