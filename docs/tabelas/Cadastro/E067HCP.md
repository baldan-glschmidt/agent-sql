# E067HCP

## Descrição

Tabelas - Integrações - Histórico Cartão Presente

---

## Resumo

- Campos: 17
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| NumCpr | String(020) | Não | Número do Cartão Presente |
| SeqHcp | Number(009,0) | Não | Sequencia de histórico de movimentos do Cartão Presente |
| DatOpr | Date | Não | Data da Operação |
| HorOpr | Number(005,0) | Sim | Hora da Operação |
| UsuOpr | Number(010,0) | Sim | Usuário responsável pela operação |
| CodFil | Number(005,0) | Sim | Código da filial |
| CodRep | Number(009,0) | Não | Código do representante |
| CodEqu | Number(003,0) | Sim | Código do equipamento fiscal |
| CroEcf | Number(006,0) | Sim | Cont. de Reinício de Operação do ECF |
| NumCoo | Number(009,0) | Sim | Contador da Ordem de Operação que emitiu o recebimento na ECF |
| VlrOpr | Number(011,2) | Sim | Valor da operação |
| TipHcp | Number(001,0) | Não | Tipo de histórico de movimento de cartão presente |
| DatVal | Date | Sim | Data de validade do cartão presente |
| SeqCan | Number(009,0) | Sim | Sequencia de cancelamento |
| ObsHcp | String(050) | Sim | Observações do histórico |
| RegPrc | String(001) | Sim | Indicativo se o registro já foi processado ou não (para controle de saldo) |

---

## Chave Primária

- CodEmp
- NumCpr
- SeqHcp

---

## Índices

### E067HCPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodEqu
- CroEcf
- NumCoo

---

## Relacionamentos

Nenhum relacionamento cadastrado.
