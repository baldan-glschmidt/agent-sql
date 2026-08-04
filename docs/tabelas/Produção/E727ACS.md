# E727ACS

## Descrição

Ficha - Roteiro - Cadastro de Acessórios p/ Operação

---

## Resumo

- Campos: 34
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodAcs | String(008) | Não | Código do Acessório que auxilia na Operação de fabricação (ferramenta, aparelho, etc.) |
| DesAcs | String(040) | Não | Descrição do Acessório |
| AbrCre | String(010) | Não | Abreviatura do Acessório |
| CodEtg | Number(004,0) | Sim | Estágio Produção |
| TipAcs | String(001) | Não | Tipo (I=Interno - da própria fábrica, E=Terceiros - Externo) |
| QtdAcs | Number(009,0) | Sim | Quantidade de Acessório |
| DesCpl | String(240) | Sim | Descrição Complementar do Acessório |
| CodCcu | String(009) | Sim | Código do Centro de Custo |
| CodUsu | Number(010,0) | Sim | Código do usuário que alterou o Registro |
| DatAlt | Date | Sim | Data da alteração do Registro |
| HorAlt | Number(005,0) | Sim | Hora da alteração do Registro |
| USU_datfab | Date | Sim | Data Fabricacao |
| USU_cusfer | Number(012,3) | Sim | Custo Ferramental |
| USU_adprea | String(250) | Sim | Adaptacao Realizada |
| USU_cusadp | Number(012,3) | Sim | Custo Adaptacao |
| USU_cusfab | Number(012,3) | Sim | Custo Fabricacao |
| USU_CodPec | String(999) | Sim | Codigo Peca |
| USU_Dtveri | Date | Sim | Data de Verificacao do Acessorio |
| USU_Codatb | String(008) | Sim | Codigo Atual do Dispositivo ATB |
| USU_Dtvali | Date | Sim | Data Fora de Linha |
| USU_Setipo | String(012) | Sim | Setor (Localizacao) e Tipo de Armazenamento |
| USU_Nrloca | String(007) | Sim | Localizacao no Tipo de Armazenamento |
| USU_filasup | Number(003,0) | Sim | Rua Setor |
| USU_lado | String(001) | Sim | Lado Rua |
| USU_codpra | Number(003,0) | Sim | Prateleira |
| USU_codniv | String(001) | Sim | Nivel |
| USU_codpos | Number(003,0) | Sim | Posicao Inicial |
| USU_SitAcs | String(001) | Sim | Situacao do Acessorio |
| USU_PesLiq | Number(011,5) | Sim | Peso líquido do produto |
| USU_PesBru | Number(011,5) | Sim | Peso bruto do produto |
| USU_CodFor | Number(009,0) | Sim | Código do Fornecedor |
| USU_DatSai | Date | Sim | Data de Saída do acessório |
| USU_DatRet | Date | Sim | Data do retorno do acessório |

---

## Chave Primária

- CodEmp
- CodAcs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
