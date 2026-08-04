# E075PFI

## Descrição

Cadastros - Produtos - Parâmetros por Filial

---

## Resumo

- Campos: 15
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPro | String(014) | Não | Código do produto |
| ProImp | Number(002,0) | Sim | Indicativo do tipo de produto para impostos |
| ClaPro | Number(003,0) | Sim | Classificação do Produto para GNRE |
| DisEnt | Number(006,0) | Sim | Código do Dispositivo Fiscal para Entradas |
| DisSai | Number(006,0) | Sim | Código do Dispositivo Fiscal para Saídas |
| CodEnt | String(060) | Sim | Código do item entrada no registro 1400 do SPED Fiscal |
| CodSai | String(060) | Sim | Código do item saída no registro 1400 do SPED Fiscal |
| IndPfl | String(001) | Sim | Indicativo se pode buscar os parâmetros fiscais da ligação Produto X Filial |
| MotDes | Number(002,0) | Sim | Motivo desoneração ICMS |
| TemRci | String(001) | Sim | Indicativo se registra entradas e saídas para controle de impostos |
| CptExl | Date | Sim | Ignorar estoque do cont. entrada e saída no invent. motivo 06 da EFD a partir de |
| DesEnt | String(250) | Sim | Descrição do item entrada no registro 1400 do SPED Fiscal |
| UniMed | String(003) | Sim | Unidade de Medida do item entrada no registro 1400 do SPED Fiscal |

---

## Chave Primária

- CodEmp
- CodFil
- CodPro

---

## Índices

### E075PFIIndice1

**Tipo:** Não unico

Campos:
- CodPro
- CodEmp

---

## Relacionamentos

### IR_E075PFI_002

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

