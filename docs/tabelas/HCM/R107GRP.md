# R107GRP

## Descrição

Perfil PDI - Grupos

---

## Resumo

- Campos: 12
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(004,0) | Não | Código do perfil |
| GrpPDI | Number(002,0) | Não | Define o grupo de informações do layout |
| TitGrp | String(100) | Sim | Título do grupo de informações |
| RotInc | String(050) | Sim | Rótulo do botão Incluir |
| RotDet | String(050) | Sim | Rótulo do botão Detalhes |
| RotExc | String(050) | Sim | Rótulo do botão Excluir |
| RotAco | String(050) | Sim | Rótulo do botão Acompanhamento |
| TitDet | String(100) | Sim | Título da tela detalhe |
| RotSal | String(050) | Sim | Rótulo do botão Salvar |
| RotCan | String(050) | Sim | Rótulo do botão Cancelar |
| RotSug | String(050) | Sim | Rótulo do botão Sugerir Plano de Ação |
| RotTCo | String(050) | Sim | Rótulo do botão Tomar conhecimento |

---

## Chave Primária

- CodPer
- GrpPDI

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R107GRP_000

**Tabela:** R107PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

