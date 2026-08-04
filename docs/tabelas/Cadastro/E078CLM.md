# E078CLM

## Descrição

Tabelas - Controle dos Lotes de Movimentos de Baixa

---

## Resumo

- Campos: 18
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatBai | Date | Não | Data da baixa do lote |
| OriBai | String(007) | Não | Nome da tela de origem do lote de baixa |
| SeqLot | Number(009,0) | Não | Sequência do lote de baixa |
| OriCha | String(007) | Sim | Nome do processo origem da baixa |
| ChvLot | String(024) | Não | Chave do lote de baixa |
| LotEst | String(001) | Não | Indicativo se o lote foi estornado |
| TipBai | Number(002,0) | Sim | Indicativo do tipo de baixa realizada |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| CodEmp | Number(004,0) | Sim | Código da empresa para lançamento do C.Pagar (ou tesouraria) de devolução |
| CodFil | Number(005,0) | Sim | Código da filial para lançamento do C.Pagar de devolução |
| NumTit | String(015) | Sim | Número do título a pagar referente à devolução de saldo |
| CodTpt | String(003) | Sim | Código do tipo do título a pagar referente à devolução de saldo |
| CodFor | Number(009,0) | Sim | Código do fornecedor do título a pagar referente à devolução de saldo |
| NumCco | String(014) | Sim | Número da conta interna para lançamento da devolução |
| DatMov | Date | Sim | Data do movimento da conta para lançamento da devolução |
| SeqMov | Number(006,0) | Sim | Sequência na data do movimento da conta para lançamento da devolução |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- DatBai
- OriBai
- SeqLot

---

## Índices

### E078CLMIndice1

**Tipo:** Unico

Campos:
- ChvLot

---

## Relacionamentos

Nenhum relacionamento cadastrado.
