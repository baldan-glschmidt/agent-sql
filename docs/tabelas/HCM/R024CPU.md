# R024CPU

## Descrição

Cargos - Órgão Público

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| DatAlt | Date | Não | Data Alteração |
| AcuCar | Number(001,0) | Sim | Cargo Acumulativo |
| ConEsp | Number(001,0) | Sim | Contagem tempo especial |
| DedExc | String(001) | Sim | Dedicação exclusiva |
| LeiCar | String(012) | Sim | Número Lei Cargo |
| DatLei | Date | Sim | Data Lei Cargo |
| SitLei | Number(001,0) | Sim | Situação gerada lei |
| SCTpQu | Number(002,0) | Sim | Tipo de Quadro - Órgão Público (e-Sfinge/SC) |

---

## Chave Primária

- EstCar
- CodCar
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024CPU_000

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R024CPU_001

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

