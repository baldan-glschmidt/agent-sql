# R351PBC

## Descrição

S-2501 - eSocial - Identificação do período e da base de cálculo dos tributos

---

## Resumo

- Campos: 14
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
| SeqPbc | Number(009,0) | Não | Sequência Identificação |
| PerRef | Date | Não | Mês/ano de referência das informações |
| VrBcCM | Number(014,2) | Sim | Base de cálculo da contrib. previdenciária sobre a rem. mensal do trabalhador |
| VrIrrf | Number(014,2) | Sim | Valor do rendimento tributável do Imposto de Renda |
| VrIr13 | Number(014,2) | Sim | Rendimento tributável do IR referente ao 13º salário - Tributação exclusiva |
| VrBc13 | Number(014,2) | Sim | Valor da base de cálculo da contribuição previdenciária referente ao 13º salário |
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

---

## Índices

### R351PBCIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
