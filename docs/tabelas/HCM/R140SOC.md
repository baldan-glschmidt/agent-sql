# R140SOC

## Descrição

Salas de Treinamento - Ocupação Extraordinária

---

## Resumo

- Campos: 14
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSla | Number(004,0) | Não | Código da Sala de Treinamento |
| DatOcu | Date | Não | Data Ocupação da Sala |
| HorIni | Number(005,0) | Não | Hora Início da Ocupação |
| HorTer | Number(005,0) | Sim | Hora Término da Ocupação |
| ComOcu | String(400) | Sim | Comentário da Ocupação Extraordinária |
| DesPro | String(500) | Sim | Providências |
| HorCbk | Number(005,0) | Sim | Horário do Início do Coffee Break |
| DesCbk | String(030) | Sim | Descrição do Coffee Break |
| CodDis | Number(003,0) | Sim | Código Disposição Lugares |
| QtdVga | Number(006,0) | Sim | Quantidade Vagas |
| CodOcu | Number(003,0) | Sim | Código do Motivo Ocupação |
| NumEmp | Number(004,0) | Sim | Empresa do Solicitante |
| TipCol | Number(001,0) | Sim | Tipo  Colaborador Solicitante |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador Solicitante |

---

## Chave Primária

- CodSla
- DatOcu
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R140SOC_000

**Tabela:** R140SLA

| Origem | Destino |
|--------|---------|
| CodSla | CodSla |

