# R017RHP

## Descrição

Postos de Trabalho - Hierarquia do Posto - Revisão da Hierarquia

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da Estrutura de Postos de trabalho |
| CodThp | Number(003,0) | Não | Código do Tipo de hierarquia do posto de trabalho |
| RevHie | Number(003,0) | Não | Código da revisão da hierarquia de postos de trabalho |
| DatRev | Date | Sim | Define a data de início da revisão da hierarquia dos Postos de trabalho |
| DatFim | Date | Sim | Define o término da revisão da hieraquia dos Postos de trabalho |
| ObsRev | String(2000) | Sim | Observações da revisão de hierarquia de Postos de trabalho |
| CodUsu | Number(009,0) | Sim | Usuário responsável pela última modificação da revisão da hierarquia |
| DthAlt | Number(014,6) | Sim | Data/Hora da última modificação da revisão da hierarquia |

---

## Chave Primária

- EstPos
- CodThp
- RevHie

---

## Índices

### R017RHPIndice1

**Tipo:** Unico

Campos:
- EstPos
- CodThp
- DatRev

---

## Relacionamentos

### IR_R017RHP_000

**Tabela:** R017EST

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |

### IR_R017RHP_001

**Tabela:** R017THP

| Origem | Destino |
|--------|---------|
| CodThp | CodThp |

