# R030ATV

## Descrição

Comissão de Representação - Reuniões - Atividades

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodMan | Number(004,0) | Não | Código do Mandato |
| DatReu | Date | Não | Data da Reunião |
| HorReu | Number(005,0) | Não | Hora de Início da Reunião |
| NumAtv | Number(004,0) | Não | Número da Atividade |
| TitAtv | String(060) | Sim | Título da Atividade |
| DesAtv | String(2000) | Sim | Descrição da Atividade |
| DatIni | Date | Não | Data de início de execução da atividade |
| DatTer | Date | Não | Data de término de execução da atividade |
| DatEnc | Date | Não | Data de Encerramento |

---

## Chave Primária

- NumEmp
- CodMan
- DatReu
- HorReu
- NumAtv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030ATV_003

**Tabela:** R030REU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodMan | CodMan |
| DatReu | DatReu |
| HorReu | HorReu |

