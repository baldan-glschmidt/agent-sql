# R351ICS

## Descrição

S-2501 - eSocial - Informações das contribuições sociais devidas à Previdência Social e Outras Entidades e Fundos

---

## Resumo

- Campos: 12
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
| SeqPbc | Number(009,0) | Não | Sequência |
| SeqIcs | Number(009,0) | Não | Sequência Informações das Contribuições |
| CodRec | Number(006,0) | Sim | CR relativo a contribuições sociais |
| ValRec | Number(014,2) | Sim | Valor correspondente ao Código de Receita - CR |
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
- SeqPbc
- SeqIcs

---

## Índices

### R351ICSIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
