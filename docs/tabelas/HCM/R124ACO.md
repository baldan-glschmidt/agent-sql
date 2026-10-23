# R124ACO

## Descrição

Colaborador - Comunicação - Anexos

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador Candidato |
| DatCom | Date | Não | Data da comunicação com o Candidato |
| HorCom | Number(005,0) | Não | Hora da comunicação com o Candidato |
| SeqAne | Number(002,0) | Não | Sequência do anexo |
| NomAne | String(250) | Sim | Nome do arquivo anexo |
| ArqAne | Image | Sim | Arquivo anexo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatCom
- HorCom
- SeqAne

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124ACO_004

**Tabela:** R124COM

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatCom | DatCom |
| HorCom | HorCom |

