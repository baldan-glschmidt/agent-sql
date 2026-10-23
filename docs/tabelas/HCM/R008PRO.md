# R008PRO

## Descrição

Processos Rubricas

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodRub | Number(009,0) | Não | Código da Rubrica |
| IdePro | Number(001,0) | Não | Identificação do Processo da Rubrica: INSS, IRRF, FGTS ou Contrib. Sindical |
| SeqPro | Number(002,0) | Não | Sequência Processo |
| CodPro | Number(009,0) | Não | Cód. processo que determina não incidência de INSS, FGTS, IRRF ou Cont. Sindical |
| CodSus | Number(014,0) | Sim | Código Suspensão |
| ExtDec | Number(001,0) | Sim | Ext. da Decisão/Sentença que determina não incidência de contrib. previdenciária |

---

## Chave Primária

- NumEmp
- CodRub
- IdePro
- SeqPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
