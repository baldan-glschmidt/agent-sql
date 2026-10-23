# R030RRH

## Descrição

Filiais da Empresa - Histórico Responsável RH

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatIni | Date | Não | Data em que assumiu a responsabilidade |
| EmpRrh | Number(004,0) | Sim | Código da empresa do responsável pelo RH |
| TipCol | Number(001,0) | Sim | Tipo do Responsável pelo RH |
| NumCad | Number(009,0) | Sim | Cadastro do Responsável pelo RH |
| DatTer | Date | Sim | Data em que encerrou a responsabilidade |
| AssDig | Image | Sim | Assinatura Digitalizada |

---

## Chave Primária

- NumEmp
- CodFil
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030RRH_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

