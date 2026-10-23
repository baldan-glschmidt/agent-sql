# R111DEF

## Descrição

Vacinação - Definição da Campanha

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodCam | Number(004,0) | Não | Código de identificação da campanha |
| SeqCam | Number(002,0) | Não | Sequência da campanha |
| DesDef | String(040) | Sim | Descrição da definição campanha de vacinação |
| DatIni | Date | Sim | Data de início da campanha |
| DatTer | Date | Sim | Data de término da campanha |
| ObsDef | String(2000) | Sim | Observações da definição da campanha |

---

## Chave Primária

- NumEmp
- CodCam
- SeqCam

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R111DEF_001

**Tabela:** R111CAM

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCam | CodCam |

