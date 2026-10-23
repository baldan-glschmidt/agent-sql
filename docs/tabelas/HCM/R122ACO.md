# R122ACO

## Descrição

Candidatos Externos - Comunicação - Anexos

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| DatCom | Date | Não | Data da comunicação com o Candidato |
| HorCom | Number(005,0) | Não | Hora da comunicação com o Candidato |
| SeqAne | Number(002,0) | Não | Sequência do anexo |
| NomAne | String(250) | Sim | Nome do arquivo anexo |
| ArqAne | Image | Sim | Arquivo anexo |

---

## Chave Primária

- NumCan
- DatCom
- HorCom
- SeqAne

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122ACO_002

**Tabela:** R122COM

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |
| DatCom | DatCom |
| HorCom | HorCom |

