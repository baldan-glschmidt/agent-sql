# R351PEN

## Descrição

S-2501 - eSocial - Informação dos beneficiários da pensão alimentícia

---

## Resumo

- Campos: 13
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
| PerApu | Date | Não | Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença |
| SeqTpt | Number(009,0) | Não | Sequência |
| SeqPar | Number(005,0) | Não | Sequência parcial |
| SeqItp | Number(009,0) | Não | Sequência Trabalhador |
| SeqIrr | Number(009,0) | Não | Sequência Informações de Imposto de Renda Retido na Fonte |
| SeqPen | Number(009,0) | Não | Sequência Beneficiários Pensão Alimentícia |
| TipRen | Number(002,0) | Sim | Tipo Rendimento |
| NumCpf | Number(011,0) | Não | Número do CPF |
| VlrPen | Number(015,2) | Sim | Valor relativo à dedução do rendimento tributável correspondente a pagamento de pensão alimentícia |
| PidExc | String(050) | Não | Identificador da pendência para execução |

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
- SeqPen

---

## Índices

### R351PENIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
