# R351ISE

## Descrição

S-2501 - eSocial - Processo Trabalhista - Rendimentos Isentos exclusivos CR 0561

---

## Resumo

- Campos: 15
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| NumPro | String(020) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| PerApu | Date | Não | Mês/ano que é devida a obrigação de pagar a parcela prevista no acordo/sentença |
| SeqTpt | Number(009,0) | Não | Sequência |
| SeqPar | Number(005,0) | Não | Sequência parcial |
| SeqItp | Number(009,0) | Não | Sequência Trabalhador |
| SeqIrr | Number(009,0) | Não | Sequência Informações de Imposto de Renda Retido na Fonte |
| SeqIse | Number(009,0) | Não | Sequência |
| VlrDia | Number(015,2) | Sim | Valor relativo a diárias |
| VlrAju | Number(015,2) | Sim | Valor relativo à ajuda de custo |
| VlrRes | Number(015,2) | Sim | Valor de indenização e rescisão, inclusive a título de PDV e acid. de trabalho |
| VlrPec | Number(015,2) | Sim | Valor relativo ao abono pecuniário |
| VlrMor | Number(015,2) | Sim | Valor relativo ao auxílio-moradia |
| PIDEXC | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- NumPro
- PerApu
- SeqTpt
- SeqPar
- SeqItp
- SeqIrr
- SeqIse

---

## Índices

### R351ISEIndice1

**Tipo:** Não unico

Campos:
- PIDEXC

---

## Relacionamentos

Nenhum relacionamento cadastrado.
