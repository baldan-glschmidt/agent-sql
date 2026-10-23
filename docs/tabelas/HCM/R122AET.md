# R122AET

## Descrição

Candidatos Externos - Etapas - Anexos

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| CodRqu | Number(009,0) | Não | Código Requisição |
| CodEta | Number(003,0) | Não | Código Etapa |
| SeqEta | Number(003,0) | Não | Sequência Etapa |
| SeqAne | Number(002,0) | Não | Sequência do anexo |
| NomAne | String(250) | Sim | Nome do arquivo anexo |
| ArqAne | Image | Sim | Arquivo anexo |

---

## Chave Primária

- NumCan
- CodRqu
- CodEta
- SeqEta
- SeqAne

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122AET_003

**Tabela:** R122CET

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |
| CodRqu | CodRqu |
| CodEta | CodEta |
| SeqEta | SeqEta |

