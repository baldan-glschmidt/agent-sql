# E076FAB

## Descrição

Cadastros - Fabricantes

---

## Resumo

- Campos: 45
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFab | String(010) | Não | Código do Fabricante |
| NomFab | String(100) | Não | Nome do Fabricante |
| ApeFab | String(050) | Não | Nome fantasia do Fabricante |
| MarFab | String(020) | Sim | Marca do Fabricante |
| TipFab | String(001) | Sim | Tipo de Fabricante |
| TipMer | String(001) | Sim | Tipo de Mercado do Fabricante |
| InsEst | String(025) | Sim | Inscrição estadual ou RG do Fabricante |
| InsMun | String(016) | Sim | Inscrição municipal do Fabricante |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF do Fabricante |
| DocIdeFab | String(014) | Sim | Número do CNPJ ou CPF do Fabricante |
| EndFab | String(035) | Sim | Endereço do Fabricante |
| CplEnd | String(200) | Sim | Complemento do endereço do Fabricante (sala, andar, etc.) |
| BaiFab | String(075) | Sim | Bairro do Fabricante |
| ZipCod | String(014) | Sim | Código da cidade do Fabricante externo - ZIP CODE |
| CepFab | Number(008,0) | Sim | CEP do Fabricante |
| CepIni | Number(008,0) | Sim | Faixa inicial do CEP da cidade do Fabricante |
| CidFab | String(060) | Sim | Cidade do Fabricante |
| SigUfs | String(002) | Sim | Estado do Fabricante |
| FonFab | String(020) | Sim | Número do telefone - 1 |
| FonFa2 | String(020) | Sim | Número do telefone - 2 |
| FonFa3 | String(020) | Sim | Número do telefone - 3 |
| FaxFab | String(020) | Sim | Número do FAX do Fabricante |
| CxaPst | Number(006,0) | Sim | Número da caixa postal do Fabricante |
| IntNet | String(100) | Sim | Endereço Eletrônico (E-Mail) |
| CodPai | String(004) | Sim | Código do país do Fabricante |
| DatCad | Date | Sim | Data do cadastramento do Fabricante |
| DatAtu | Date | Sim | Data da última alteração do cadastro do Fabricante |
| SitFab | String(001) | Não | Situação do Fabricante |
| CodMot | Number(006,0) | Sim | Código do motivo da situação do Fabricante |
| ObsMot | String(250) | Sim | Observação do motivo da situação do Fabricante |
| UsuMot | Number(010,0) | Sim | Usuário responsável pelo motivo da situação do Fabricante |
| DatMot | Date | Sim | Data do motivo da situação do Fabricante |
| HorMot | Number(005,0) | Sim | Hora do motivo da situação do Fabricante |
| QtdDcm | Number(003,0) | Sim | Quantidade de dias para o cálculo do consumo médio. |
| EenFab | String(018) | Sim | Código do endereço do fabricante |
| PrzGfa | Number(004,0) | Sim | Prazo de garantia de fábrica dada pelo fabricante |
| PrzTfa | Number(004,0) | Sim | Prazo de garantia de fábrica dada pelo fabricante para troca |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| NenFab | String(060) | Sim | Número do Endereço do Fabricante |
| NumIdf | String(040) | Sim | Número de identificação fiscal |

---

## Chave Primária

- CodFab

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
