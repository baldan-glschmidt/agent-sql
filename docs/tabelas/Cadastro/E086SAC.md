# E086SAC

## Descrição

Cadastros - Sacados

---

## Resumo

- Campos: 34
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSac | Number(014,0) | Sim | Número do CNPJ ou CPF do sacado |
| DocIdeSac | String(014) | Sim | Número do CNPJ ou CPF do sacado |
| TipSac | String(001) | Não | Tipo do sacado |
| NomSac | String(100) | Não | Nome do sacado |
| ApeSac | String(050) | Sim | Nome fantasia do sacado |
| EndSac | String(035) | Sim | Endereço do sacado |
| NumEnd | Number(005,0) | Sim | Número do Endereço do Sacado |
| CplEnd | String(200) | Sim | Complemento do endereço do sacado (sala, andar, etc.) |
| CepSac | Number(008,0) | Sim | CEP do sacado |
| CepIni | Number(008,0) | Sim | Faixa inicial do CEP da cidade do sacado |
| BaiSac | String(075) | Sim | Bairro do sacado |
| CidSac | String(060) | Sim | Cidade do sacado |
| SigUfs | String(002) | Sim | Sigla do estado do sacado |
| FonSac | String(020) | Sim | Número do telefone do sacado |
| FaxSac | String(020) | Sim | Número do FAX do sacado |
| CxaPst | Number(006,0) | Sim | Número da caixa postal do sacado |
| IntNet | String(100) | Sim | Endereço eletrônico (E-Mail) |
| DatCad | Date | Sim | Data do cadastramento do sacado |
| DatAtu | Date | Sim | Data da última alteração do cadastro do sacado |
| SitSac | String(001) | Não | Situação do sacado |
| EenSac | String(018) | Sim | Código do endereço do sacado |
| EndCob | String(100) | Sim | Endereço de cobrança do sacado |
| CplCob | String(200) | Sim | Complemento do endereço de cobrança do sacado |
| CepCob | Number(008,0) | Sim | CEP do endereço de cobrança do sacado |
| CidCob | String(060) | Sim | Cidade do endereço de cobrança do sacado |
| EstCob | String(002) | Sim | Estado do endereço de cobrança do sacado |
| NenCob | String(060) | Sim | Número do Endereço de Cobrança do Sacado |
| BaiCob | String(075) | Sim | Bairro de cobrança do sacado |
| IniCob | Number(008,0) | Sim | Faixa inicial do CEP do endereço de cobrança do sacado |
| EenCob | String(018) | Sim | Código do endereço de cobrança do sacado |
| CelSac | String(020) | Sim | Número do telefone celular do sacado |
| SacBlo | String(001) | Sim | Indicativo para Sacado Bloqueado |
| MotBlo | String(150) | Sim | Descrição do Motivo do Bloqueio |
| IdeUni | String(050) | Não | Identificador único alfanumérico |

---

## Chave Primária

- IdeUni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
