# R234AVA

## Descrição

Evento - Avaliação de Eficácia - Avaliado

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| CodPes | Number(009,0) | Não | Código da Pessoa |
| EmpAvl | Number(004,0) | Sim | Código da empresa do avaliador |
| TipAvl | Number(001,0) | Sim | Tipo colaborador avaliador |
| CadAvl | Number(009,0) | Sim | Cadastro do colaborador avaliador |
| SitAef | Number(001,0) | Sim | Situação da avaliação de eficácia |
| TreEfi | String(001) | Sim | Indica se o treinamento foi eficaz |
| DatLim | Date | Sim | Data limite para efetuar a avaliação de eficácia |

---

## Chave Primária

- CodEvn
- CodPes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234AVA_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

### IR_R234AVA_001

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

