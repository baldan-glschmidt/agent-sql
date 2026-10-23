# R010SER

## Descrição

Tipos de Serviços

---

## Resumo

- Campos: 15
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSer | Number(003,0) | Não | Código do Serviço |
| NomSer | String(030) | Sim | Nome do Serviço |
| DesSer | String(060) | Sim | Descrição do Serviço |
| CalIss | String(001) | Sim | Calcular ISS |
| CalIns | String(001) | Sim | Calcular INSS |
| CalIrf | String(001) | Sim | Calcular IRRF |
| TipRen | Number(003,0) | Sim | Tipo de Rendimento |
| ForTri | Number(002,0) | Sim | Forma de Tributação |
| TipSer | Number(001,0) | Sim | Tipo de Serviço |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| CodPro | Number(009,0) | Sim | Código do Processo |
| CodSus | Number(014,0) | Sim | Código Suspensão |
| ExtDec | Number(001,0) | Sim | Ext. da Decisão/Sentença que determina não incidência de contrib. previdenciária |
| IniLim | Date | Sim | Início da Aplicação da Liminar |
| FimLim | Date | Sim | Fim da Aplicação da Liminar |

---

## Chave Primária

- CodSer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
