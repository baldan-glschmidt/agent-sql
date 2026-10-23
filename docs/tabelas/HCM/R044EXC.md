# R044EXC

## Descrição

Códigos de Cálculo - Exceções

---

## Resumo

- Campos: 19
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| SeqExc | Number(002,0) | Não | Sequência |
| ExcCal | Number(001,0) | Sim | Tipo de Exceção do Código de Cálculo |
| AbrExc | String(100) | Sim | Abrangência |
| DatPag | Date | Sim | Data do Pagamento |
| IniCmp | Date | Sim | Data Início Período Folha |
| FimCmp | Date | Sim | Data Final Período Folha |
| IniVtr | Date | Sim | Início competência vtr |
| FimVtr | Date | Sim | Fim competência vtr |
| IniApu | Date | Sim | Data Início Período Apuração Ponto |
| FimApu | Date | Sim | Data Final Período Apuração Ponto |
| IapCom | Date | Sim | Data Início Apuração Comissões |
| FapCom | Date | Sim | Data Final Apuração Comissões |
| IniAce | Date | Sim | Data Início Período Acerto Ponto |
| FimAce | Date | Sim | Data Final Período Acerto Ponto |
| IniFvt | Date | Sim | Início Competência Faltas Vtr |
| FimFvt | Date | Sim | Fim Competência Faltas Vtr |
| CodLot | Number(004,0) | Sim | Código do Lote |

---

## Chave Primária

- NumEmp
- CodCal
- SeqExc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R044EXC_001

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

