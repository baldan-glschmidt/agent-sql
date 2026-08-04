# E069CCS

## Descrição

Tabelas - Seguros - Coberturas de seguro

---

## Resumo

- Campos: 21
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| DesCob | String(250) | Sim | Descrição da cobertura do seguro |
| PerFra | Number(005,2) | Sim | Percentual para cálculo da franquia da cobertura |
| DesLmi | String(250) | Sim | Descrição do limite máximo de indenização |
| CarCob | Number(003,0) | Sim | Carência (em dias) da cobertura |
| DesCcb | String(050) | Sim | Descrição da carência da cobertura |
| PerIof | Number(005,2) | Sim | Percentual de IOF aplicado sobre o prêmio |
| IdeCse | Number(009,0) | Não | Idenficador do registro do cadastro do seguro |
| CobSeg | String(020) | Sim | Código da cobertura na seguradora |
| CapMin | Number(011,2) | Sim | Capital segurado mínimo |
| CapMax | Number(011,2) | Sim | Capital segurado máximo |
| PmiCob | Number(011,2) | Sim | Prêmio mínimo da cobertura |
| PmaCob | Number(011,2) | Sim | Prêmio máximo da cobertura |
| PrfCob | Number(005,2) | Sim | Percentual de referência da cobertura |
| PreCob | Number(005,2) | Sim | Percentual do prêmio do seguro aplicável à cobertura |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E069CCSIndice2

**Tipo:** Não unico

Campos:
- IdeCse

---

## Relacionamentos

### IR_E069CCS_007

**Tabela:** E069CSE

| Origem | Destino |
|--------|---------|
| IdeCse | IdeUni |

