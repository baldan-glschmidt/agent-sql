# E017DRL

## Descrição

Tabelas - Configuração de leiaute do Recebimento Eletrônico - Campos

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeRel | Number(009,0) | Não | Identificador de registro |
| NomCam | String(060) | Não | Nome do campo de origem |
| DesCam | String(100) | Não | Descrição do campo de origem |
| TabDes | String(030) | Sim | Tabela de destino na base de dados do ERP |
| CamDes | String(030) | Sim | Campo de destino na base de dados do ERP |
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

### E017DRLIndice1

**Tipo:** Unico

Campos:
- IdeRel
- NomCam
- TabDes
- CamDes

---

## Relacionamentos

### IR_E017DRL_001

**Tabela:** E017REL

| Origem | Destino |
|--------|---------|
| IdeRel | IdeUni |

