# R351COL

## Descrição

S-2501 - eSocial - Relação de Colaboradores Processados

---

## Resumo

- Campos: 11
- Chave Primária: 8 campo(s)
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
| SeqCad | Number(009,0) | Não | Sequência Código Trabalhador |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
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
- SeqCad

---

## Índices

### R351COLIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
