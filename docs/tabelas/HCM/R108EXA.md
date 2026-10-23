# R108EXA

## Descrição

Exames

---

## Resumo

- Campos: 43
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodExa | Number(004,0) | Não | Código Exame |
| DesExa | String(030) | Sim | Descrição Exame |
| CodAmb | Number(008,0) | Sim | Código AMB |
| CodCBH | Number(008,0) | Sim | Classificação Hierarquizada de Procedimentos Médicos |
| SexExa | String(001) | Sim | Restrição por Sexo |
| MesNor | Number(003,0) | Sim | Meses Exame Normal |
| PriNor | Number(003,0) | Sim | Meses do Primeiro Exame Normal |
| MesIns | Number(003,0) | Sim | Meses Exame de Insalubridade |
| PriIns | Number(003,0) | Sim | Meses Primeiro Exame Insalubridade |
| MesPer | Number(003,0) | Sim | Meses Exame de Periculosidade |
| PriPer | Number(003,0) | Sim | Meses Primeiro Exame de Periculosidade |
| FaiMen | Number(002,0) | Sim | Faixa Etária Menor |
| MesMen | Number(003,0) | Sim | Meses Exame Menor Faixa Etária |
| PriMen | Number(003,0) | Sim | Meses Primeiro Exame Menor Faixa Etária |
| FaiMai | Number(002,0) | Sim | Faixa Etária Maior |
| MesMai | Number(003,0) | Sim | Meses Exame Maior Faixa Etária |
| PriMai | Number(003,0) | Sim | Período Primeiro Exame Maior Faixa Etária |
| MesAcp | Number(003,0) | Sim | Meses Acompanhamento Demitidos |
| PriAcp | Number(003,0) | Sim | Meses do Primeiro Exame de Acompanhamento de Demitidos |
| DurAcp | Number(003,0) | Sim | Duração do Acompanhamento Demitidos |
| VenExa | Number(003,0) | Sim | Tempo de Vencimento Exame Pré-admissional(em meses) |
| CodReg | Number(003,0) | Sim | Código da regra para interpretação do exame |
| ConPpp | String(001) | Sim | Considera este exame p/perfil profissiográfico previdenciário |
| ExaAud | String(001) | Sim | Identifica se o Exame é Audiométrico |
| ExaTox | String(001) | Sim | Identifica se o Exame é Toxicológico |
| ParNor | Number(003,0) | Sim | Código do Parecer considerado como Normal |
| ParAlt | Number(003,0) | Sim | Código do Parecer considerado como Alterado |
| RegCon | Number(003,0) | Sim | Regra para criticar a alteração dos itens de Resultado |
| DesAna | String(079) | Sim | Descrição de qual análise é realizada |
| MatBio | String(006) | Sim | Descrição do material biológico |
| QuaNr7 | String(001) | Sim | Exame está relacionado no quadro I da NR7 |
| AprRes | String(001) | Sim | Define se será apresentada a coluna Resultado padrão |
| InfRef | String(001) | Sim | Permite informação de valores de ref no resultado. |
| QtdCas | Number(001,0) | Sim | Define a Quantidade de Casas decimais do exame(0-5) |
| PreExa | String(2000) | Sim | Identifica as recomendações de preparação para o exame |
| CodMab | Number(001,0) | Sim | Material Biológico |
| CodAnQ | String(004) | Sim | Análise |
| CodAgQ | Number(002,0) | Sim | Agente Químico |
| ConQd3 | String(001) | Sim | Define se deve considerar exame no relatório do Quadro III da NR7 |
| CodPro | Number(008,0) | Sim | Código do Procedimento Diagnóstico |
| ProObs | String(999) | Sim | Observação sobre o procedimento diagnóstico realizado |
| TipExa | Number(001,0) | Sim | Define se o exame é considerado clínico ou complementar |
| UtiAss | String(001) | Sim | Utiliza assinatura eletrônica |

---

## Chave Primária

- CodExa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
