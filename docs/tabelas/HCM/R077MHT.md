# R077MHT

## Descrição

Resultado da Avaliação de Habilidades Técnicas

---

## Resumo

- Campos: 15
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CmpAva | Date | Não | Competência da Avaliação |
| CodHte | String(006) | Não | Código da Habilidade Técnica |
| NotPrf | Number(005,2) | Sim | Nota Média atingida na Habilidade |
| PerPrf | Number(005,2) | Sim | % atingido na Habilidade |
| NotDom | Number(005,2) | Sim | Nota Média de Domínio |
| PerDom | Number(005,2) | Sim | % Médio Domínio |
| PerApf | Number(005,2) | Sim | % atingido nos Requisitos de Aperfeiçoamento |
| PerFor | Number(005,2) | Sim | % atingido nos Requisitos de Formação |
| VerCer | String(001) | Sim | OBSOLETO 5.4.1.39 - Indica que a Habilidade foi Certificada através desta Avaliação |
| CmpHab | Date | Sim | Competência do Histórico de Habilidade gerado na Certificação |
| LotRes | Number(009,0) | Sim | Número do lote em que foi gerado o Resultado |
| CodCic | Number(003,0) | Sim | Código do ciclo de avaliação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpAva
- CodHte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R077MHT_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R077MHT_004

**Tabela:** R077HTE

| Origem | Destino |
|--------|---------|
| CodHte | CodHte |

