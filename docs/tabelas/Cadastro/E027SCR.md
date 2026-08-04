# E027SCR

## Descrição

Cadastro da situação e classificação tributária do CBS/IBS (cClassTrib)

---

## Resumo

- Campos: 22
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador do cClassTrib |
| CodStr | String(003) | Não | Código da situação tributária do CBS/IBS |
| DesStr | String(255) | Não | Descrição da situação tributária do CBS/IBS |
| CodCla | String(003) | Não | Código da classificação tributária do CBS/IBS |
| DesCla | String(255) | Não | Descrição da classificação tributária do CBS/IBS |
| AliZeC | String(001) | Sim | Alíquota zero da CBS |
| RedCbs | Number(005,2) | Sim | Percentual de redução da CBS |
| AliZeI | String(001) | Sim | Alíquota zero do IBS |
| RedIbs | Number(005,2) | Sim | Percentual de redução do IBS |
| StrCla | String(006) | Não | Código da cClassTrib (Situação + Classificação) |
| VigIni | Date | Não | Vigência inicial |
| VigFin | Date | Sim | Vigência final |
| AliFcb | Number(008,4) | Sim | Alíquota fixa da CBS |
| AliFiu | Number(008,4) | Sim | Alíquota fixa do IBS UF |
| AliFim | Number(008,4) | Sim | Alíquota fixa do IBS Município |
| TipMon | Number(001,0) | Sim | Tipo de tributação monofásica |
| EstCre | String(001) | Sim | Indicador de estorno de crédito da cClassTrib |
| AjuCom | String(001) | Sim | Indicador de ajuste de competência da cClassTrib |
| TraCre | String(001) | Sim | Indicador de transferência de crédito da cClassTrib |
| ExiTri | String(001) | Sim | Indica se exige tributação |
| DifTri | String(001) | Sim | Indica se possui diferimento |
| TipRed | String(002) | Sim | Indica o tipo de redução (Base de Calculo ou Alíquota) |

---

## Chave Primária

- IdeUni

---

## Índices

### E027SCR_UK

**Tipo:** Unico

Campos:
- CodStr
- CodCla
- VigIni
- VigFin

---

## Relacionamentos

Nenhum relacionamento cadastrado.
