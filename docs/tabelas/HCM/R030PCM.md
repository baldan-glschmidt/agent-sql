# R030PCM

## Descrição

Filiais da Empresa - Histórico Responsável PCMSO

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
| CodFil | Number(006,0) | Não | Código da Filial |
| DatIni | Date | Não | Data em que assumiu a responsabilidade |
| EmpPcm | Number(004,0) | Não | Código da empresa do responsável pelo PCMSO |
| TipCol | Number(001,0) | Não | Tipo do Responsável pelo PCMSO |
| NumCad | Number(009,0) | Não | Cadastro do Responsável pelo PCMSO |
| DatTer | Date | Sim | Data em que encerrou a responsabilidade |
| AssDig | Image | Sim | Assinatura Digitalizada |

---

## Chave Primária

- NumEmp
- CodFil
- DatIni
- EmpPcm
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030PCM_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

