# R351ADV

## Descrição

S-2501 - eSocial - Identificação dos advogados

---

## Resumo

- Campos: 14
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
| SeqAdv | Number(009,0) | Não | Sequência Identificação Advogados |
| TipIns | Number(001,0) | Não | Tipo Inscrição |
| NumIns | Number(014,0) | Sim | Número de Inscrição - Obsoleto |
| CfjIns | String(014) | Sim | Número de Inscrição |
| VlrAdv | Number(015,2) | Sim | Valor das despesas com advogados, se houver |
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
- SeqAdv

---

## Índices

### R351ADVIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
