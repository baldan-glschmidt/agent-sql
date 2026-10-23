# R351IDE

## Descrição

S-2501 - eSocial - Informações de dependentes não cadastrados pelo S-2200/S-2205/S-2300

---

## Resumo

- Campos: 15
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
| SeqIde | Number(009,0) | Não | Sequência Dependente não cadastrado |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| DatNas | Date | Sim | Data Nascto Dependente |
| NomDep | String(040) | Sim | Nome do Dependente |
| DepIrr | String(001) | Sim | Somente informar este campo em caso de dependente do trabalhador para fins de dedução de seu rendimento tributável pelo Imposto de Renda |
| TipDep | Number(002,0) | Sim | Tipo de Dependente eSocial |
| DesDep | String(100) | Sim | Descrição da dependência |
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
- SeqIde

---

## Índices

### R351IDEIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
