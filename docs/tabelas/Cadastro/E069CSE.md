# E069CSE

## Descrição

Tabelas - Seguros - Cadastro de seguro

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeCsi | Number(009,0) | Não | Identificador de registro |
| DiaRec | Number(003,0) | Sim | Quantidade de dias para recuperação do seguro |
| EleCob | String(250) | Sim | Descrição da elegibilidade da cobertura |
| ModSeg | Number(002,0) | Sim | Modalidade de cadastramento do seguro |
| InfCas | String(001) | Sim | Indicativo se informa capital segurado para as coberturas |
| InfPse | String(001) | Sim | Indicativo se informa prêmio mínimo e máximo para as coberturas |
| PrzVal | Number(003,0) | Sim | Prazo de validade (em meses) |
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

### E069CSEIndice1

**Tipo:** Não unico

Campos:
- IdeCsi

---

## Relacionamentos

### IR_E069CSE_001

**Tabela:** E080CSI

| Origem | Destino |
|--------|---------|
| IdeCsi | IdeUni |

